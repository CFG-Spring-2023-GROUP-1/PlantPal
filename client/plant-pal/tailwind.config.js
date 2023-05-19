/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{js,jsx,ts,tsx}"],
	theme: {
		extend: {
			fontFamily: {
				manrope: "'Manrope', sans-serif",
				kaushan: "'Kaushan Script', cursive",
			},
			colors: {
				gray: {
					light: "rgba(237, 237, 237, 0.35)",
					20: "#EDEDED",
					30: "#333333",
					50: "#F0F0F0",
					100: "#786983",
					200: "#AEAEAE",
					600: "#696969",
				},
			},
		},
	},
	plugins: [],
};
