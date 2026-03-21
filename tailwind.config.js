/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  theme: {
    extend: {
      colors: {
        'ottelio-gold': '#D4AF37',
        'ottelio-dark': '#1A1A1A',
      },
      fontFamily: {
        serif: ['"Playfair Display"', 'Georgia', 'serif'],
        sans: ['"Inter"', 'Helvetica', 'Arial', 'sans-serif'],
      }
    },
  },
  plugins: [],
}