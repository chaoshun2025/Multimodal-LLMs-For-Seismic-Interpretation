There are different ways to generate text and 2D/3D image pairs.
Here I use pynoddy. Another way is to using Gempy.
Recently William Davis from Terri.AI tried to use PyPDF2 and PyMUpdf to extract text and images from pdf reports or papers.
Then he used LLama to consolidate the text and dump DSL styple for Gempy. Later he can generate 3D structure maps.

                                 PyNoddy
          Text---------------------------------------> 2D/3D Image



![image](https://github.com/chaoshun2025/Multimodel-VLMs-For-Seismic-Interpretation/edit/main/DataPrep/img10_seismic.jpg)





what William did is

     PyPDF2              LLM                              LLM              Gempy
PDF ---------> Text --------------->Consolidated Text --------->DSL data-----------> 3D structures

![image](https://github.com/user-attachments/assets/a0fa775a-8e06-43f3-b13f-5451ad93b9d4)
