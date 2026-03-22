/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{html,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'villa-gold': '#B8860B', // Oro scuro per i titoli
        'villa-black': '#050505', // Nero profondo per sfondi
        'villa-soft': '#F5F5F5',  // Grigio chiarissimo per testi leggibili
      },
      fontFamily: {
        'serif': ['Playfair Display', 'serif'], // Font elegante per titoli
        'sans': ['Inter', 'sans-serif'],        // Font moderno per testi lunghi
      },
    },
  },
  plugins: [],
}