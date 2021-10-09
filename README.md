# COVID19-bedbooking-API

I created this API using Flask, MongoDB(for database), Python(code), 
Here i have shared a JSON file which  contains Bed List (patient_critical_level,pincode,hospital,timeslot) and a app.py 
file which contains codes for Booking of Bed, Booking rescheduling, Cancel booking.

-The code is tested on Postman
-GET Url to see bed list : http://localhost:5000/Bedlist
-POST Url to book bed: http://localhost:5000/Bookbed
-PUT Url to reschedule booking: http://localhost:5000/Reschedule/61612bc3b144ea77545c281a
-it is the ID of an element that is to be updated : 61612bc3b144ea77545c281a
-DELETE Url to Cancel a booking an element : http://localhost:5000/Cancelbooking/61614e67f84e1972569b2cc2
-it is the ID of an element that is to be deleted : 61614e67f84e1972569b2cc2


![Screenshot (364)](https://user-images.githubusercontent.com/52618132/136654646-6dec25b9-a6d2-4819-a600-3bf0e301d4ea.png)

![Screenshot (366)](https://user-images.githubusercontent.com/52618132/136654794-bb56ceef-1cb1-4857-ac83-a381d09b174e.png)

![Screenshot (367)](https://user-images.githubusercontent.com/52618132/136654796-0fb08199-d626-47db-a157-8a15211bde03.png)

![Screenshot (368)](https://user-images.githubusercontent.com/52618132/136654797-6b710bd6-0095-4acc-97ee-a9d30da35d6d.png)

