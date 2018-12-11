# CSC-322-Project


  We want to develop a document sharing system such that group members can collaborate on the same documents without causing inconsistencies. There are three types of users in this system: Super User (SU), Ordinary User (OU) and Guest (GU). 
SU:

[ ]	update membership
[ ]	maintain a list of taboo words
[ ]	unlock any locked document
[ ]	process complaints about OU's
[ ]	have all privileges reserved for OUs inside any group
OU:
•	create new document(s), the creator of a document is the owner of the document and can invite other OUs to update it, and decide if the document is open to the public (can be seen by everyone), restricted (can only be viewed as read-only by GU's and edited by OU's), shared (viewed/edited by OU's who are invited) and private
•	an OU can accept or deny the invitation(s) placed by other OUs for their documents
•	lock a shared document for updating, only one OU can lock a document successfully, the system should indicate which OU is updating the document
•	update a successfully locked document, and then assign a unique version sequence number and remember who and when makes the updates
•	unlock a shared document locked by him/herself
•	file complaints to the owner of a document about other OUs'updates or to the SU about the owner of the documents
•	as the owner of a document deal with complaints filed by other OUs (remove some OUs who were invited before)
•	unlock the locked documents s/he owns that is being updated by others
•	search own file(s) based on (partial) keyword
•	search information about other OUs based on name and/or interests.
•	have all privileges for GUs

GU:
•	read open document(s), retrieve old version(s) of open document(s) and complains about those documents.
•	send suggestions to SU about taboo words
•	apply to be an OU that is to be confirmed or rejected by SU, in the application his/her name, technical interests should be submitted.

constraints:
•	there is only ONE current version for any document
•	for simplicity there is only one word for each line in all documents 
•	only the editing command(s) are saved for older versions with three possible actions: add, delete and update. For instance, if the file doc_1.txt contains one line "the", and doc_2.txt contains three lines "welcome \n the \n world\n", then your system only saves doc_2.txt, doc_1.history saves the commands "delete 1; delete 3" which changes doc_2.txt into doc_1.txt. Your system generates the history command file based on the difference.
•	the retrieval of older versions of documents should be done by your system based on the current version and possibly a sequence of history files. 
•	any word(s) belonging to the taboo list (maintained by SU) are replaced by UNK by the system, and the one who use these words are warned automatically, s/he should update the document next time s/he log in the system as the first job (all other activities are blocked)
•	a creative feature worthy of 15% is required for each system, one possible feature could be allowing more than word per line, or speech-based document updating is allowed, or some machine learning features to render this system adaptable/evolving by itself thru usage. 
•	a GUI is required, different users should have their own page populated by his/her picture and 3 most recent documents. For a brand-new user, the 3 most popular (most read and/or updated) files in the system are shown.
