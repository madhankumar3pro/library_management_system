Library Management System: 

The Library Management System is designed to manage books and users in a library. It 
provides functionality to add, update, delete, and search for books and users. Additionally, it 
handles the check-in and check-out of books, late-fees, maintaining logs for these 
transactions. The system ensures that only authorized managers can access and manipulate 
the data. 
late-fees of each book per day charge is 10 rupees. 
Design Decisions: 
1. Separation of Concerns: 
o Classes and methods are organized based on functionality. Book Manager and 
User Manager handle book and user data respectively, while Storage integrates 
these with file operations. 
2. Data Persistence: 
o Data is stored in JSON files (books.json, users.json, and book_in_out.json) to ensure 
persistence across sessions. 
3. Security: 
o Manager credentials are secured with hashed passwords using SHA-256. 
4. User Interface: 
o A text-based menu-driven interface is provided for interaction. 


Architecture: 
• Book-Manager: Manages book data including adding, updating, deleting, and 
searching books. 
• User-Manager: Manages user data including adding, updating, deleting, and 
searching users. 
• Storage: Integrates Book-Manager and User-Manager with file operations and manages 
book check-in/check-out logs. 
• main.py: Entry point of the application, providing a menu-driven interface for the 
manager to interact with the system.

Flow Chart of Library management 

![image](https://github.com/madhankumar3pro/library_management_system/assets/87332206/1acb81a1-0503-48d1-a1c7-e68aa5f9a22f)

