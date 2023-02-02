<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Document</title>
    <style>
    body {background-color: powderblue;font-size:20px;}
    h1   {color: blue;}
    p    {color: red;}
</style>
</head>
<body>

        <div class="mt-20 mb-20">
            
            <div class="row mt-20 mb-20">
                <div class="col-3"></div>
                <div class="col-1"><h1>No</h1></div>
                <div class="col-2"><h1>ID</h1></div>
                <div class="col-2"><h1>Image</h1></div>
                <div class="col-2"><h1>Classification</h1></div>
                <div class="col-3"></div>
            </div>
            <hr>
                   {% for new in newlist %}
                    <div class="row mt-10 mb-10"> 
                            <div class="col-3"></div>
                            <div class="col-1">{{new+1}}</div>
                        
                            <div class="col-2">{{newlist[new][0]}}</div>
                        
                            <div class='col-2'><img src='{{newlist[new][1]}}' alt='Image' width='200' height='200'></div>
                            <div class="col-2">{{msg[new]}}</div>
                            <div class="col-3"></div>
                    </div>
                    <hr>
                    {% endfor %}
            
        
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    
</body>
</html>