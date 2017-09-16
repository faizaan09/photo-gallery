# photo-gallery

## Overall Description

### 1. Product  Perspective
This product has been designed to improve the storage and access efficiency of user’s photos. It aims at implementing a system similar to an online gallery. Online galleries show photos in various ways, Phileikones will store the images of the user and show them as a part of an online gallery.  
Product  Functions
Also show the activity diagram, dfd level 0 and sequence diagram

### 2. Following are the main functions of the system :
Register and Log in, as per the norms mentioned in the form
Upload photos and creates albums in the database
Allow users to add other users to contribute to particular albums.
Show all the albums associated with the user in fancy ways.

### 3. User Classes and Characteristics
The application supports naïve users. All users fall into the same category. All users can have their own personal albums as well as shared albums. There will be an administrator to monitor the overall system.

### 4. Operating Environment
Following are the specifications of the Client System:

#### 4.1 Any OS
Web Browser: Firefox/Chrome/Opera/ Internet Explorer/ Edge / Safari
JQuery 

#### 4.2 Following are the specifications of the Server System:

 4.2.1 Python version 3.4 <br />
 4.2.2 Support for Django Framework <br />
 4.2.3 SQLite DBMS <br />

### 5. Design and Implementation Constraints
The first constraint is that there is no valid verification of the image content provided by the user, copyright infringement is possible. The user can’t upload multiple images simultaneously.

The second constraint is that the system currently runs on the local machine . Hence the size of database is restricted to the size of the given machine.
