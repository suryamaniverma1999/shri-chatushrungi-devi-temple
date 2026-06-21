from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>ShriChatushrungiDeviTemple.in</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #fff8e1;
            color: #333;
        }

        header {
            background: linear-gradient(to right, #b71c1c, #ff9800);
            color: white;
            text-align: center;
            padding: 40px 20px;
        }

        header h1 {
            font-size: 38px;
            margin: 0;
        }

        header h2 {
            margin-top: 10px;
            font-size: 28px;
        }

        nav {
            background: #6d1b1b;
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
            font-weight: bold;
        }

        .hero {
            text-align: center;
            padding: 60px 20px;
            background: #ffe0b2;
        }

        .hero h2 {
            color: #b71c1c;
            font-size: 32px;
        }

        .section {
            max-width: 1000px;
            margin: auto;
            padding: 30px 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .card h2 {
            color: #b71c1c;
        }

        .details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 15px;
        }

        .box {
            background: #fff3cd;
            padding: 18px;
            border-radius: 10px;
            border-left: 5px solid #ff9800;
        }

        iframe {
            width: 100%;
            height: 350px;
            border: 0;
            border-radius: 12px;
        }

        footer {
            background: #212121;
            color: white;
            text-align: center;
            padding: 25px;
        }

        button {
            background: #b71c1c;
            color: white;
            border: none;
            padding: 12px 22px;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #8b0000;
        }
    </style>
</head>

<body>

<header>
    <h1>ShriChatushrungiDeviTemple.in</h1>
    <h2>श्री चतुश्रुंगी देवी मंदिर</h2>
    <p>Senapati Bapat Road, Pune, Maharashtra</p>
</header>

<nav>
    <a href="#about">About</a>
    <a href="#timing">Timing</a>
    <a href="#details">Details</a>
    <a href="#location">Location</a>
    <a href="#contact">Contact</a>
</nav>

<div class="hero">
    <h2>Welcome to Shri Chatushrungi Devi Temple</h2>
    <p>A peaceful hillside temple dedicated to Goddess Chatushrungi Devi.</p>
    <button onclick="alert('Jai Mata Di 🙏')">Jai Mata Di</button>
</div>

<div class="section" id="about">
    <div class="card">
        <h2>About Temple</h2>
        <p>
            Shri Chatushrungi Devi Temple is one of the famous Hindu temples in Pune.
            The temple is located on a hillside and is known for its steep entrance steps,
            vibrant temple facade and peaceful surroundings.
        </p>
        <p>
            Devotees visit the temple to seek blessings of Goddess Chatushrungi Devi.
        </p>
    </div>
</div>

<div class="section" id="timing">
    <div class="card">
        <h2>Temple Timing</h2>
        <p><b>Status:</b> Open</p>
        <p><b>Closing Time:</b> 9:00 PM</p>
        <p><b>Best Time to Visit:</b> Morning and Evening Aarti</p>
    </div>
</div>

<div class="section" id="details">
    <div class="card">
        <h2>Temple Details</h2>

        <div class="details">
            <div class="box">
                <h3>Rating</h3>
                <p>4.7 ⭐</p>
            </div>

            <div class="box">
                <h3>Reviews</h3>
                <p>15,713</p>
            </div>

            <div class="box">
                <h3>Temple Type</h3>
                <p>Hindu Temple</p>
            </div>

            <div class="box">
                <h3>Location</h3>
                <p>Pune, Maharashtra</p>
            </div>
        </div>
    </div>
</div>

<div class="section">
    <div class="card">
        <h2>Address</h2>
        <p>
            971, Senapati Bapat Rd, Sheti Mahamandal,
            Shivaji Co-operative Housing Society, Ramoshivadi,
            Gokhalenagar, Pune, Maharashtra 411016
        </p>
    </div>
</div>

<div class="section" id="location">
    <div class="card">
        <h2>Location Map</h2>
        <iframe
            src="https://www.google.com/maps?q=Shri%20Chatushrungi%20Devi%20Temple%20Pune&output=embed"
            loading="lazy">
        </iframe>
    </div>
</div>

<div class="section" id="contact">
    <div class="card">
        <h2>Contact</h2>
        <p><b>Website:</b> ShriChatushrungiDeviTemple.in</p>
        <p><b>Address:</b> Senapati Bapat Road, Pune, Maharashtra</p>
    </div>
</div>

<footer>
    <p>© 2026 ShriChatushrungiDeviTemple.in</p>
    <p>Made with Python Flask</p>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)