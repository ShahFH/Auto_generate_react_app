import os

# Step 1: Set up a new React app using Create React App (CRA)
os.system('npx create-react-app my-app')
os.chdir('my-app')

# Step 2: Install Tailwind CSS and its dependencies
os.system('npm install tailwindcss postcss autoprefixer')

# Step 3: Create a Tailwind CSS configuration file
os.system('npx tailwindcss init')

# Step 4: Update the Tailwind CSS configuration
with open('tailwind.config.js', 'r') as file:
    lines = file.readlines()

with open('tailwind.config.js', 'w') as file:
    for line in lines:
        if line.startswith('purge:'):
            file.write("  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],\n")
        else:
            file.write(line)

# Step 5: Create a postcss configuration file
with open('postcss.config.js', 'w') as file:
    file.write("module.exports = {\n")
    file.write("  plugins: [\n")
    file.write("    require('tailwindcss'),\n")
    file.write("    require('autoprefixer'),\n")
    file.write("  ],\n")
    file.write("};\n")

# Step 6: Update the index.css file
with open('src/index.css', 'w') as file:
    file.write("@import 'tailwindcss/base';\n")
    file.write("@import 'tailwindcss/components';\n")
    file.write("@import 'tailwindcss/utilities';\n")

# Step 7: Update the index.js file
with open('src/index.js', 'r') as file:
    lines = file.readlines()

with open('src/index.js', 'w') as file:
    for line in lines:
        if line.startswith('import './index.css';'):
            file.write("import './index.css';\n")
        else:
            file.write(line)

# Step 8: Start the development server
os.system('npm start')
