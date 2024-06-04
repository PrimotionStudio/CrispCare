window.onload = function () {
	const get_date = (hours) => {
		let now = new Date();
		now.setHours(now.getHours() + hours);
		let _date =
			now.getFullYear() +
			"-" +
			("0" + (now.getMonth() + 1)).slice(-2) +
			"-" +
			("0" + now.getDate()).slice(-2) +
			"T" +
			("0" + now.getHours()).slice(-2) +
			":" +
			("0" + now.getMinutes()).slice(-2);

		return _date;
	};
	document.getElementById("start_date").value = get_date(0);
	document.getElementById("end_date").value = get_date(2);
};
const decline = (hk_id, booking_id) => {
	const formData = new FormData();
	formData.append("hk_id", hk_id);
	formData.append("booking_id", booking_id);
	fetch({
		url: "/bookings/decline",
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded",
		},
		body: new URLSearchParams(formData),
	})
		.then((response) => {
			alert("Declined");
		})
		.catch((error) => console.error(error));
};

const terminate = (hk_id, booking_id) => {
	const formData = new FormData();
	formData.append("hk_id", hk_id);
	formData.append("booking_id", booking_id);
	fetch({
		url: "/bookings/terminate",
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded",
		},
		body: new URLSearchParams(formData),
	})
		.then((response) => {
			alert("Terminated");
		})
		.catch((error) => console.error(error));
};
