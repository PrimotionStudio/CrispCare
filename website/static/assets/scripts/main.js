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
