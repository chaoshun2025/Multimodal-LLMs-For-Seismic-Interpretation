from datasets import Dataset, Features, Value, Sequence,DatasetDict,load_dataset
import json
from PIL import Image
import os

# definition of features
features = Features({
    "image_path": Value("string"),
    "caption": Value("string"),
})

# load json file to create dataset
def load_custom_dataset(json_file_path, image_folder_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    dataset_data = {
        "image_path": [],
        "caption": [],
    }
    for annotation in data["annotations"]:
        image_path = os.path.join(image_folder_path, annotation["filename"])
        
        dataset_data["image_path"].append(image_path)
        dataset_data["caption"].append(annotation["caption"])
    
    # create dataset
    dataset = Dataset.from_dict(dataset_data, features=features)
    return dataset

# call
json_file_path = "./data/captions.json"  # JSON filepath
image_folder_path = "./data/images/"  # image filepath
dataset = load_custom_dataset(json_file_path, image_folder_path)
print(dataset)

#  split dataset and use 80% as training dataset
dataset_split = dataset.train_test_split(test_size=0.2)

# further split for validation and testing as 10% and 10%
test_valid_split = dataset_split['test'].train_test_split(test_size=0.5)

# finalized the training, validate and test dataset
train_dataset = dataset_split['train']
valid_dataset = test_valid_split['train']
test_dataset = test_valid_split['test']

# create a DatasetDict object
dataset_dict = DatasetDict({
    'train': train_dataset,
    'validation': valid_dataset,
    'test': test_dataset
})


# QC the size of each dataset
print(f"Training dataset size: {len(train_dataset)}")
print(f"Validation dataset size: {len(valid_dataset)}")
print(f"Test dataset size: {len(test_dataset)}")
print(dataset_dict)

# variable to save train, validation and test dataset
train_path = "./data/train.json"
validation_path = "./data/validation.json"
test_path = "./data/test.json"

# save train, valid and test dataset from dataset_dict 
def save_dataset_to_json(dataset_dict, train_path, validation_path, test_path):
    # save train dataset
    with open(train_path, 'w', encoding='utf-8') as f:
        for item in dataset_dict['train']:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')
    
    # save validation dataset
    with open(validation_path, 'w', encoding='utf-8') as f:
        for item in dataset_dict['validation']:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')
    
    # save testing dataset
    with open(test_path, 'w', encoding='utf-8') as f:
        for item in dataset_dict['test']:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

# writeout
save_dataset_to_json(dataset_dict, train_path, validation_path, test_path)

# load the image
def load_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return image

# load the dataset
dataset_path = "./data"
train_dataset = load_dataset('json', data_files={'train': f'{dataset_path}/train.json'})['train']
validation_dataset = load_dataset('json', data_files={'validation': f'{dataset_path}/validation.json'})['validation']
test_dataset = load_dataset('json', data_files={'test': f'{dataset_path}/test.json'})['test']

# define a mapping function to load image to example['image']
def preprocess_example(example):
    example['image'] = load_image(example['image_path'])
    return example

# apply mapping function to three datasets
train_dataset = train_dataset.map(preprocess_example)
validation_dataset = validation_dataset.map(preprocess_example)
test_dataset = test_dataset.map(preprocess_example)

# create DatasetDict
dataset_dict = DatasetDict({
    'train': train_dataset,
    'validation': validation_dataset,
    'test': test_dataset
})

#dump to local disk
dataset_dict.save_to_disk('./data/dataset_full/')

# qc the 1st element
print(dataset_dict['train'][0])

#load from disk
from datasets import load_from_disk
train_dataset_new = load_from_disk('./data/dataset_full/train')
validation_dataset_new = load_from_disk('./data/dataset_full/validation')
test_dataset_new = load_from_disk('./data/dataset_full/test')

print(train_dataset_new[0])
print(validation_dataset_new[0])
print(test_dataset_new[0])

