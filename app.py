from flask import Flask, render_template

app = Flask(__name__)

restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 7,
        "location": "Manila",
        "restaurant_name": "Restaurant Seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 8,
        "location": "Davao",
        "restaurant_name": "Restaurant Eight",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 9,
        "location": "Bohol",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 10,
        "location": "Tagbilaran",
        "restaurant_name": "Restaurant Ten",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 11,
        "location": "Las Piñas",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 12,
        "location": "Muntinlupa",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": ""
    },{
        "id": 13,
        "location": "Valenzuela",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 14,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": ""
    },{
        "id": 15,
        "location": "Marikina",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 16,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": ""
    },{
        "id": 17,
        "location": "Baguio",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 18,
        "location": "Bacolod",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": ""
    },{
        "id": 19,
        "location": "Iloilo City",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 20,
        "location": "Cagayan de Oro",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": ""
    },{
        "id": 21,
        "location": "General Santos",
        "restaurant_name": "Restaurant Twenty-One",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 22,
        "location": "Butuan",
        "restaurant_name": "Restaurant Twenty-Two",
        "status": "Open",
        "image_url": ""
    },{
        "id": 23,
        "location": "Zamboanga City",
        "restaurant_name": "Restaurant Twenty-Three",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 24,
        "location": "Dagupan",
        "restaurant_name": "Restaurant Twenty-Four",
        "status": "Open",
        "image_url": ""
    },{
        "id": 25,
        "location": "Naga",
        "restaurant_name": "Restaurant Twenty-Five",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 26,
        "location": "Batangas City",
        "restaurant_name": "Restaurant Twenty-Six",
        "status": "Open",
        "image_url": ""
    },{
        "id": 27,
        "location": "Tacloban",
        "restaurant_name": "Restaurant Twenty-Seven",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 28,
        "location": "Legazpi",
        "restaurant_name": "Restaurant Twenty-Eight",
        "status": "Open",
        "image_url": ""
    },{
        "id": 29,
        "location": "Olongapo",
        "restaurant_name": "Restaurant Twenty-Nine",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 30,
        "location": "Lucena",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": ""
    },{
        "id": 31,
        "location": "Puerto Princesa",
        "restaurant_name": "Restaurant Thirty-One",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 32,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Thirty-Two",
        "status": "Open",
        "image_url": ""
    },{
        "id": 33,
        "location": "Angeles City",
        "restaurant_name": "Restaurant Thirty-Three",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 34,
        "location": "Tarlac City",
        "restaurant_name": "Restaurant Thirty-Four",
        "status": "Open",
        "image_url": ""
    },{
        "id": 35,
        "location": "Calamba",
        "restaurant_name": "Restaurant Thirty-Five",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 36,
        "location": "Lipa City",
        "restaurant_name": "Restaurant Thirty-Six",
        "status": "Open",
        "image_url": ""
    },{
        "id": 37,
        "location": "San Fernando",
        "restaurant_name": "Restaurant Thirty-Seven",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 38,
        "location": "Ormoc",
        "restaurant_name": "Restaurant Thirty-Eight",
        "status": "Open",
        "image_url": ""
    },{
        "id": 39,
        "location": "Sorsogon",
        "restaurant_name": "Restaurant Thirty-Nine",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 40,
        "location": "Roxas City",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": ""
    },{
        "id": 41,
        "location": "Dumaguete",
        "restaurant_name": "Restaurant Forty-One",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 42,
        "location": "Koronadal",
        "restaurant_name": "Restaurant Forty-Two",
        "status": "Open",
        "image_url": ""
    },{
        "id": 43,
        "location": "Cotabato City",
        "restaurant_name": "Restaurant Forty-Three",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 44,
        "location": "Santiago",
        "restaurant_name": "Restaurant Forty-Four",
        "status": "Open",
        "image_url": ""
    },{
        "id": 45,
        "location": "Vigan",
        "restaurant_name": "Restaurant Forty-Five",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 46,
        "location": "Laoag",
        "restaurant_name": "Restaurant Forty-Six",
        "status": "Open",
        "image_url": ""
    },{
        "id": 47,
        "location": "Malaybalay",
        "restaurant_name": "Restaurant Forty-Seven",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 48,
        "location": "Baybay",
        "restaurant_name": "Restaurant Forty-Eight",
        "status": "Open",
        "image_url": ""
    },{
        "id": 49,
        "location": "Pagadian",
        "restaurant_name": "Restaurant Forty-Nine",
        "status": "Closed",
        "image_url": ""
    },{
        "id": 50,
        "location": "Dipolog",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": ""
    },
]



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)