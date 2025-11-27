# Vue Bootstrap App

## Description
This project is a Vue.js application that utilizes Bootstrap for styling. It provides a simple interface for managing vehicle information, allowing users to view, add, and edit vehicle details.

## Project Structure
```
vue-bootstrap-app
├── src
│   ├── main.js               # Entry point of the Vue application
│   ├── App.vue               # Root component of the application
│   ├── components            # Contains reusable components
│   │   ├── Navbar.vue        # Navigation bar component
│   │   ├── VehicleList.vue   # Component to display a list of vehicles
│   │   └── VehicleForm.vue   # Form component for adding/editing vehicles
│   ├── views                 # Contains view components
│   │   └── Home.vue          # Home view of the application
│   ├── assets                # Contains static assets
│   │   └── styles
│   │       └── custom.scss   # Custom styles written in SCSS
│   └── router                # Contains routing configuration
│       └── index.js          # Vue Router setup
├── public
│   └── index.html            # Main HTML file
├── package.json              # Project metadata and dependencies
├── vite.config.js            # Vite configuration file
├── .gitignore                # Files to ignore in Git
└── README.md                 # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vue-bootstrap-app
   ```

2. **Install dependencies**
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

## Usage

1. **Run the development server**
   ```bash
   npm run dev
   ```
   This will start the Vite development server. You can access the application at `http://localhost:3000`.

2. **Build for production**
   To create a production build, run:
   ```bash
   npm run build
   ```

## Features
- Responsive design using Bootstrap
- Vehicle management with add/edit functionality
- Dynamic routing with Vue Router

## Contributing
Feel free to submit issues or pull requests for any improvements or features you'd like to see!

## License
This project is licensed under the MIT License.