<html>
<head>
<style>

    body {
        text-align: center;
        margin-top: 50px;
        font-size: 25px;
    }

    h1 {
        color: red;
    }

    iframe {
        width:100%;
        height: 65%;
        border:0px;
    }
</style>
</head>


<body>
    <h1>Covid Stats!</h1><br>
    <form method="POST">
        <label >Enter a Country Name</label><br><br>
        <input placeholder="Country Name" name="text">
        <input type="submit">
    </form>
    <iframe src="{{ image }}"></iframe>


    <p>You have {{ count }} Visitors.</p>
</body>
</html>