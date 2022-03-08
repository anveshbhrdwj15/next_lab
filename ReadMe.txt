ReadMe

Problem_1_1
The solution to this problem is in jupyter notebook. I have created two codes. One is assuming the input as string and extracting numbers using Re module. The other one is assuming input as dictionary and looping through keys and values and extracting the numbers.

Problem_1_2
Steps I took to solve this problem:
+ Input .CSV using Streamlit web interface
+read input and apply cleaning functions to the text data
+get sentiment score for text review and stars
+return the dataframe where text review is positive and star review is negative

I have used StreamLit to deploy the model on my local computer. The notebook is saved as both .py and .ipynb. for the deployment to work, I have to run the .py file using "streamlit run problem_1_2.py". A webpage will be opened asking for .csv input. The input is given by uploading a .csv file. Here i have used the given dataset as input.Applied "Review Cleaning", "Remove Emoji", "Getpolarity","getAnalysis", "Star_senti" to the required columns. Please Refer problem_1_2.ipynb file for these functions. The output is displayed on the webpage. I have not taken accuracy of the pridiction into accout. The accuracy can be achieved by more fine-tuning the data. I have focused more on the implementation.
URL: http://localhost:8501/   once you run streamlit from command prompt 


Problem_1_3:

Q: Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)?

Keywords should be strategically placed throughout content to make it clear both to the search engines and the users what topics the content will cover. This means that keywords should be used naturally throughout the content, but they should also be included in the headings and tags

Q: Does APP ID (Also known as package name) play any role in ranking?  


Yes If the Keyword is used in the name of AppID, it plays an important role in Ranking


Q: Any other pattern or good questions that you can think of and answer?

The other thing is date of last description change also plays an important role in ranking.

Problem_2_1

Please refer Problem_2_1.ipynb. The steps i took are:
+clean the data for punctuations
+import pre-trained BERT model
+Encode the text using BERT encoder
+using model, predict the output
+return the output 



Q:Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 

A:
In my previous job, I was working as a system administrator. There was this situation where i have to work on virtualization software called VMware
I have to upgrade the baremetal OS (ESXi) and  upgrade the vCenter server software. In the mean process, I have to upgrade the hardware as well.
Its like doing multiple upgrades at the same time. I have it all planned out but was not prepared for surprises. During the upgrade, One of the new hardware stopped responding
Thats like loss of view for some vms. So to solve the problem, I had to take the situation with calm mind and take it slowly. The steps I took was
see if any other hardware is compatible? Can i recover VMs using backup? can i be able to copy the vms from one hardware to other hardware as see if i can restore.
So combination of recovering VMs from backup, copying vms did the job.


Q:Formally, a vector space V' is a subspace of a vector space V if
V' is a vector space
every element of V′ is also an element of V.
Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
The set of pairs (a, a + 1) for all real a
The set of pairs (a, b) for all real a ≥ b
The set of pairs (a, 2a) for all real a
The set of pairs (a, b) for all non-negative real a,b


A:

The set of pairs (a, b) for all non-negative real a,b























"""