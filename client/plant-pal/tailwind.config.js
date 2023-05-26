module.exports = {
	content: ["./src/**/*.{js,jsx,ts,tsx}"],
	theme: {
		extend: {
			fontFamily: {
				manrope: "'Manrope', sans-serif",
				kaushan: "'Kaushan Script', cursive",
			},
			colors: {
				green: {
					light: "rgba(237, 237, 237, 0.35)",
					20: "#F4F7F3",
					30: "#D2DECE",
					50: "#A5BE9D",
					100: "#719765",
					200: "#4F7868",
					300: "#698C7A",
					400: "#526B56",
					500: "#536E49"
				},
				brown: {
					light: "rgba(237, 237, 237, 0.35)",
					20: "#F4F7F3",
					30: "#D2DECE",
					50: "#A5BE9D",
					100: "#F7F3F3",
					200: "#C6A9A9",
					300: "#698C7A",
					400: "#526B56",
					500: "#536E49"
				},
			},
			fontSize: {
				'2xs': '10px'
			}
		},
	},
	plugins: [],
};
