from flask import Flask

app = Flask(__name__)

portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My Portfolio</title>
    <style>
        /* Reset and base */
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #121212;
            color: #e0e0e0;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        a {
            color: #1db954;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }

        header {
            background: #222;
            padding: 1rem 2rem;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 10;
            border-bottom: 2px solid #1db954;
        }
        header h1 {
            margin: 0;
            font-weight: 700;
            font-size: 2rem;
            color: #1db954;
        }

        nav {
            margin-top: 0.5rem;
        }
        nav a {
            margin: 0 1rem;
            font-weight: 600;
            font-size: 1rem;
            color: #e0e0e0;
        }

        main {
            max-width: 900px;
            margin: 2rem auto;
            padding: 0 1rem 3rem 1rem;
        }

        section {
            margin-bottom: 4rem;
        }

        h2 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #1db954;
            padding-bottom: 0.5rem;
        }

        #about p {
            font-size: 1.1rem;
        }

        .projects-list {
            display: grid;
            grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
            gap: 1.5rem;
        }

        .project {
            background: #222;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.7);
            transition: transform 0.3s ease;
        }
        .project:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(29,185,84,0.7);
        }
        .project h3 {
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: #1db954;
        }
        .project p {
            font-size: 1rem;
        }
        .project a {
            display: inline-block;
            margin-top: 0.75rem;
            font-weight: 600;
        }

        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }
        .skill {
            background: #1db954;
            color: #121212;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-weight: 600;
            box-shadow: 0 2px 6px rgba(0,0,0,0.5);
        }

        #contact form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-width: 400px;
        }
        #contact label {
            font-weight: 600;
        }
        #contact input, #contact textarea {
            padding: 0.5rem;
            border-radius: 5px;
            border: none;
            font-size: 1rem;
            resize: vertical;
        }
        #contact input:focus, #contact textarea:focus {
            outline: 2px solid #1db954;
        }
        #contact button {
            background: #1db954;
            border: none;
            color: #121212;
            font-weight: 700;
            padding: 0.75rem;
            border-radius: 30px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        #contact button:hover {
            background: #17a74a;
        }

        footer {
            text-align: center;
            padding: 1rem;
            border-top: 1px solid #333;
            color: #666;
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 600px) {
            header h1 {
                font-size: 1.5rem;
            }
            nav a {
                margin: 0 0.5rem;
                font-size: 0.9rem;
            }
            main {
                margin: 1rem auto;
                padding: 0 0.5rem 2rem 0.5rem;
            }
            .projects-list {
                grid-template-columns: 1fr;
            }
            #contact form {
                max-width: 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Jane Doe Portfolio</h1>
        <nav>
            <a href="#about">About Me</a>
            <a href="#projects">Projects</a>
            <a href="#skills">Skills</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Hello! I'm Jane Doe, a passionate software developer specializing in web and mobile applications. I love crafting intuitive and beautiful user experiences.</p>
        </section>

        <section id="projects">
            <h2>Projects</h2>
            <div class="projects-list">
                <div class="project">
                    <h3>Project One</h3>
                    <p>A web application that helps users track their habits and daily goals.</p>
                    <a href="https://github.com/janedoe/project-one" target="_blank">View on GitHub</a>
                </div>
                <div class="project">
                    <h3>Project Two</h3>
                    <p>A cross-platform mobile app for real-time chat with end-to-end encryption.</p>
                    <a href="https://github.com/janedoe/project-two" target="_blank">View on GitHub</a>
                </div>
                <div class="project">
                    <h3>Project Three</h3>
                    <p>Portfolio website showcasing my skills and projects with a modern design.</p>
                    <a href="https://janedoe.com" target="_blank">Visit Website</a>
                </div>
            </div>
        </section>

        <section id="skills">
            <h2>Skills</h2>
            <div class="skills-list">
                <div class="skill">Python</div>
                <div class="skill">JavaScript</div>
                <div class="skill">React</div>
                <div class="skill">Flask</div>
                <div class="skill">Django</div>
                <div class="skill">HTML & CSS</div>
                <div class="skill">SQL</div>
                <div class="skill">Git</div>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <form onsubmit="submitForm(event)">
                <label for="name">Name</label>
                <input id="name" name="name" type="text" required placeholder="Your name" />
                
                <label for="email">Email</label>
                <input id="email" name="email" type="email" required placeholder="Your email" />
                
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="4" required placeholder="Write your message here..."></textarea>
                
                <button type="submit">Send</button>
            </form>
            <p id="form-status" style="margin-top:8px;"></p>
        </section>
    </main>

    <footer>
        &copy; 2024 Jane Doe. All rights reserved.
    </footer>

    <script>
        function submitForm(event) {
            event.preventDefault();
            const status = document.getElementById('form-status');
            status.style.color = '#1db954';
            status.textContent = 'Thank you for your message! I will get back to you soon.';
            event.target.reset();
        }
    </script>
</body>
</html>
"""
