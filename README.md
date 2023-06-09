# commerce
### Project Description

"Bid It" is an eBay-like e-commerce auction website that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist". This project was developed back in December 2020 as a small personal project made for fun and exercise with basic full stack web development technologies, with no intention of being used in production or for any commercial use. The current version of the website is designed to be desktop-only. 
The website allows the user to view active listings without having an account, while the other services provided require the user to be signed in.

![Screenshot_11](https://user-images.githubusercontent.com/47897459/229382466-6239a7d0-cd84-4d88-9534-46162c6b2924.png)


The signed in user could also add some of the active listings on a personal watchlist, in order to keep track of the auction procedure more easily. In addition, for easier navigation, the user is able to browse listings based on their category(four basic categories are included in the current version). 


![Screenshot_12](https://user-images.githubusercontent.com/47897459/229383014-68559dd3-2d35-4b5e-9047-8fcc6e846fed.png)

If the user is interested about a product, they are able to view some details provided by the owner, as well as place a bid in order to compete against other interested users.

![Screenshot_13](https://user-images.githubusercontent.com/47897459/229382828-ab97799e-c917-4049-b934-77d4ed93d297.png)
 Also, the user is able to post a comment about the product, or review the already existing comments made by other users, by visiting the comment section of the current listing.
![Screenshot_14](https://user-images.githubusercontent.com/47897459/229383111-93d27d8c-7a13-4075-864a-00c32aabae7f.png)

Finally the user is able to create their own listings and control the auction's closing time. When an auction is closed, the winner is notified when visiting the product's page.

### How to run

In order to run the app locally on your desktop,follow these steps:

1. Clone the repository to you local terminal.
2. Navigate to the project folder using the command-line(or powershell for Windows users).
3. Install the required dependencies(assuming python is already installed) using the command ```pip install -r requirements.txt```
4. Start the app using the command ```python manage.py runserver```. If the local server has started successfully you should see a message saying "Starting development server at http://127.0.0.1:8000/" amongst the rest of the message.
5. Open a web browser and type the following URL ```http://127.0.0.1:8000/```. If all the previous steps are executed correctly, you should be able to see a live demo of the webpage.
6. Have fun!

