#Campus Exchange: A Second-Hand Exchange Platform
Campus Exchange is a dedicated platform for college students to buy, sell, and auction second-hand items. Designed with security, affordability, and user-friendliness in mind, it fosters sustainability and community engagement within academic institutions.
________________________________________
Features
User Roles
•	Superuser/Admin:
o	Manage users, products, and auctions.
o	Credentials:
	Username: admin
	Password: admin
o	Alternate Credentials:
	Username: superuser
	Password: superuser
•	Students:
o	Register using their college credentials.
o	Access platform features like product listings, auctions, and chats.
Key Functionalities
1.	User Authentication:
o	Secure registration linked to college email.
o	Password guidelines for enhanced security.
2.	Product Listings:
o	Add, delete, and manage products.
o	Filter products by category, condition, and location.
3.	Auction System:
o	Bid on products with live timers and real-time updates.
4.	Chat System:
o	Direct communication between buyers and sellers.
5.	College-Based Filtering:
o	Ensures transactions within the same academic institution for trust and convenience.
________________________________________
Installation Guide
Prerequisites
•	Software:
o	Python: v3.12.7
o	Django: v5.1.1
o	SQLite3: v3.45
•	Hardware:
o	Processor: 2.0 GHz
o	RAM: 8GB
o	Disk Space: 10GB
Steps to Set Up
1.	Clone the Repository:
<git clone  https://github.com/EnggProjects/Campus_Exchange>
2.	Install Dependencies:
o	Ensure all versions match the ones mentioned above.
3.	Database Migration:
o	Run these on your VSCode Terminal, Inside the :
<python manage.py makemigrations>
<python manage.py migrate>
4.	Start the Server:
<python manage.py runserver>
5.	Access the Platform:
o	Open http://127.0.0.1:8000 in your browser or click on the link that’s now displayed in your terminal
o	Use the provided credentials to log in.
________________________________________
Usage Guide
Superuser/Admin Access
1.	Log in using the admin credentials.
2.	Use the Django Admin Panel (/admin) for:
o	Adding, deleting, or updating users.
o	Managing products and auctions.
o	Creating groups for users
o	Other Administrative tasks
Student Access
1.	Register:
o	Fill out the registration form with college details.
2.	Login:
o	Use the registered credentials.
3.	Explore Features:
o	Add, Exchange and Auction Products.
o	View and filter products.
o	Bid on auctions.
o	Chat with sellers for product inquiries.
________________________________________
Contribution
Feel free to fork this repository, create issues, and submit pull requests for improvements.
________________________________________

