# Campus Exchange: A Second-Hand Exchange Platform

Campus Exchange is a dedicated platform for college students to buy, sell, and auction second-hand items. Designed with security, affordability, and user-friendliness in mind, it fosters sustainability and community engagement within academic institutions.

---

## Features

### User Roles

- **Superuser/Admin**:
  - Manage users, products, and auctions.
  - **Credentials**:
    - Username: `admin`
    - Password: `admin`
  - **Alternate Credentials**:
    - Username: `superuser`
    - Password: `superuser`
  
- **Students**:
  - Register using their college credentials.
  - Access platform features like product listings, auctions, and chats.

### Key Functionalities

1. **User Authentication**:
   - Secure registration linked to college email.
   - Password guidelines for enhanced security.

2. **Product Listings**:
   - Add, delete, and manage products.
   - Filter products by category, condition, and location.

3. **Auction System**:
   - Bid on products with live timers and real-time updates.

4. **Chat System**:
   - Direct communication between buyers and sellers.

5. **College-Based Filtering**:
   - Ensures transactions within the same academic institution for trust and convenience.

---

## Installation Guide

### Prerequisites

- **Software**:
  - Python: `v3.12.7`
  - Django: `v5.1.1`
  - SQLite3: `v3.45`

- **Hardware**:
  - Processor: `2.0 GHz`
  - RAM: `8GB`
  - Disk Space: `10GB`

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/EnggProjects/Campus_Exchange
## Installation Guide

### Install Dependencies

Ensure all versions match the ones mentioned above.

### Database Migration

Run these commands on your VSCode Terminal:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2.  Start the Server
   ```bash
python manage.py runserver
   ```

3. Access the Platform
    Open http://127.0.0.1:8000 in your browser or click on the link displayed in your terminal.
    Use the provided credentials to log in.

### Usage Guide
#### Superuser/Admin Access:
Log in using the admin credentials.
Use the Django Admin Panel (/admin) for:
Adding, deleting, or updating users.
Managing products and auctions.
Creating groups for users.
Other administrative tasks.

#### Student Access
Register:
Fill out the registration form with college details.
Login:
Use the registered credentials.
Explore Features:
Add, exchange, and auction products.
View and filter products.
Bid on auctions.
Chat with sellers for product inquiries.

## Contribution
Feel free to fork this repository, create issues, and submit pull requests for improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
