# MultiModel VLMs for Seismic Interpretation
1) Data Preparation for Multimodel LLMs for Seismic Interpretation
2) MLLM training

3) Test on image44_seismic.jpg

The interpretation from the finetuned model is as follow,

"This seismic reflection image features gently dipping sedimentary layers that form a broad syncline fold structure. The reflections curve downward toward the center of the image, confirming symmetric compression and sediment accumulation in a marine environment. This type of geometry suggests a tilted crustal wedge configuration typical of regional fold-and-thrust belts.
"
The ground truth caption is 
"This seismic image shows a broad syncline structure composed of gently dipping sedimentary layers. The reflections curve downward toward the center of the image, characteristic of compressional folding. A prominent angular unconformity at the top truncates the folded strata, indicating a major erosional surface formed after folding but before the deposition of the overlying tilted layers. The entire sequence, including the unconformity, dips slightly to the right, suggesting later regional tilting.
"

The original seismic image is shown as,

<img width="660" alt="image" src="https://github.com/user-attachments/assets/92616f92-f453-49a6-a30b-5062518144e8" />

You are welcome to use this small dataset to multimodel LLMs for seismic interpretation tests.

Please acknowledge me if you can.
