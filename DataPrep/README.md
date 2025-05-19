There are different ways to generate text and 2D/3D image pairs.
Here I use pynoddy. Similar try can use Gempy and Stanford's synthesis toolbox and Shell's synthetic package.

Then he used LLama to consolidate the text and dump DSL styple for Gempy. Later he can generate 3D structure maps.

                                 PyNoddy
          Text---------------------------------------> 2D/3D Image


<img width="766" alt="image" src="https://github.com/user-attachments/assets/a76a63c2-26a3-4970-afee-6ea18049cc2c" />

Recently LLM has been used to generate visual text pairs. We can use PyPDF2 and PyMUpdf to extract text and images from pdf reports or papers, use LLM to consolidate the extract texts and since LLM has been improved to understand the structure data, we can use LLM to generate a structure data and then we used these structured data to build the subsurface structure and seismic images.

Recently William Davis from Terri.AI tried in this direction. What William did is

     PyPDF2              LLM                              LLM              Gempy
PDF ---------> Text --------------->Consolidated Text --------->DSL data-----------> 3D structures

![image](https://github.com/user-attachments/assets/a0fa775a-8e06-43f3-b13f-5451ad93b9d4)
