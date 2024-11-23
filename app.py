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
        "image_url": "https://plus.unsplash.com/premium_photo-1661953124283-76d0a8436b87?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 8,
        "location": "Davao",
        "restaurant_name": "Restaurant Eight",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 9,
        "location": "Bohol",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1497644083578-611b798c60f3?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 10,
        "location": "Tagbilaran",
        "restaurant_name": "Restaurant Ten",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 11,
        "location": "Las Piñas",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://plus.unsplash.com/premium_photo-1670984939096-f3cfd48c7408?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 12,
        "location": "Muntinlupa",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1494346480775-936a9f0d0877?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 13,
        "location": "Valenzuela",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1508424757105-b6d5ad9329d0?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 14,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 15,
        "location": "Marikina",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1474898856510-884a2c0be546?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 16,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1661883237884-263e8de8869b?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D"
    },{
        "id": 17,
        "location": "Baguio",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1485182708500-e8f1f318ba72?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 18,
        "location": "Bacolod",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1661433201283-fcb240e88ad4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 19,
        "location": "Iloilo City",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1551632436-cbf8dd35adfa?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 20,
        "location": "Cagayan de Oro",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1505275350441-83dcda8eeef5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 21,
        "location": "General Santos",
        "restaurant_name": "Restaurant Twenty-One",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 22,
        "location": "Butuan",
        "restaurant_name": "Restaurant Twenty-Two",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1686090448301-4c453ee74718?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 23,
        "location": "Zamboanga City",
        "restaurant_name": "Restaurant Twenty-Three",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1488992783499-418eb1f62d08?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 24,
        "location": "Dagupan",
        "restaurant_name": "Restaurant Twenty-Four",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1502998070258-dc1338445ac2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 25,
        "location": "Naga",
        "restaurant_name": "Restaurant Twenty-Five",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1481833761820-0509d3217039?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 26,
        "location": "Batangas City",
        "restaurant_name": "Restaurant Twenty-Six",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1525610553991-2bede1a236e2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 27,
        "location": "Tacloban",
        "restaurant_name": "Restaurant Twenty-Seven",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1526069631228-723c945bea6b?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 28,
        "location": "Legazpi",
        "restaurant_name": "Restaurant Twenty-Eight",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1681841594224-ad729a249113?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjV8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 29,
        "location": "Olongapo",
        "restaurant_name": "Restaurant Twenty-Nine",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 30,
        "location": "Lucena",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1421622548261-c45bfe178854?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 31,
        "location": "Puerto Princesa",
        "restaurant_name": "Restaurant Thirty-One",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1511081692775-05d0f180a065?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 32,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Thirty-Two",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1723491285855-f1035c4c703c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjl8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 33,
        "location": "Angeles City",
        "restaurant_name": "Restaurant Thirty-Three",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1502301103665-0b95cc738daf?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzB8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 34,
        "location": "Tarlac City",
        "restaurant_name": "Restaurant Thirty-Four",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1416453072034-c8dbfa2856b5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 35,
        "location": "Calamba",
        "restaurant_name": "Restaurant Thirty-Five",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1488324346298-5ad3d8f96d0d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzJ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 36,
        "location": "Lipa City",
        "restaurant_name": "Restaurant Thirty-Six",
        "status": "Open",
        "image_url": "https://plus.unsplash.com/premium_photo-1670984940113-f3aa1cd1309a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 37,
        "location": "San Fernando",
        "restaurant_name": "Restaurant Thirty-Seven",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1489209909448-8926a2640f1f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzR8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 38,
        "location": "Ormoc",
        "restaurant_name": "Restaurant Thirty-Eight",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1517638851339-a711cfcf3279?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzV8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 39,
        "location": "Sorsogon",
        "restaurant_name": "Restaurant Thirty-Nine",
        "status": "Closed",
        "image_url": "https://plus.unsplash.com/premium_photo-1673108852141-e8c3c22a4a22?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzd8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 40,
        "location": "Roxas City",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1489528792647-46ec39027556?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzh8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 41,
        "location": "Dumaguete",
        "restaurant_name": "Restaurant Forty-One",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1520209268518-aec60b8bb5ca?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 42,
        "location": "Koronadal",
        "restaurant_name": "Restaurant Forty-Two",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1517740642137-bc729c123aa5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 43,
        "location": "Cotabato City",
        "restaurant_name": "Restaurant Forty-Three",
        "status": "Closed",
        "image_url": "https://plus.unsplash.com/premium_photo-1661954531673-440d23a6eb79?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDF8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 44,
        "location": "Santiago",
        "restaurant_name": "Restaurant Forty-Four",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1569096651661-820d0de8b4ab?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDJ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 45,
        "location": "Vigan",
        "restaurant_name": "Restaurant Forty-Five",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1537047902294-62a40c20a6ae?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDN8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 46,
        "location": "Laoag",
        "restaurant_name": "Restaurant Forty-Six",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1484156818044-c040038b0719?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 47,
        "location": "Malaybalay",
        "restaurant_name": "Restaurant Forty-Seven",
        "status": "Closed",
        "image_url": "https://plus.unsplash.com/premium_photo-1674147605306-7192b6208609?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDV8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 48,
        "location": "Baybay",
        "restaurant_name": "Restaurant Forty-Eight",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1504718855392-c0f33b372e72?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDZ8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 49,
        "location": "Pagadian",
        "restaurant_name": "Restaurant Forty-Nine",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },{
        "id": 50,
        "location": "Dipolog",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://images.unsplash.com/photo-1522336572468-97b06e8ef143?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDh8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D"
    },
]



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)