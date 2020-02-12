<template>
	<div>
		<div class="diary-day-select">
			<i class="fas fa-chevron-left" @click="go_left()"/>
			<VueCtkDateTimePicker v-model="current_date"
												class="diary-day-picker"
												:only-date="true"
												format="YYYY-MM-DD"
												formatted="ll"
												@validate="test"
												@is-hidden="test"
			>
				<span class="diary-day-picker-title">today</span>
			</VueCtkDateTimePicker>
			<i class="fas fa-chevron-right" @click="go_right()"/>
		</div>
	</div>
</template>

<script>
export default {
	name: "DiaryDaySelect",
	props: {
		value: String
	},
	data() {
		return {
			current_date: this.value
		};
	},
	methods: {
		test: function() {
			this.$emit('input', this.current_date);
		},
		go_left: function() {
			let date = new Date(this.current_date);		
			let yesterday = date.getDate() - 1
			this.current_date = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+yesterday;
			console.log(this.current_date);
		},
		go_right: function() {
			let date = new Date(this.current_date);		
			let yesterday = date.getDate() + 1
			this.current_date = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+yesterday;
			console.log(this.current_date);
		},
	},
	created() {
		// let today = new Date();
		// this.current_date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();		
	}
}
</script>

<style scoped>

.diary-day-select {
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 20px;
	margin: 30px;
	margin-top: 50px;
}

.diary-day-picker {
	display: flex;
	justify-content: center;
		width: 200px;
	margin: 0 20px;
}

.diary-day-picker-title {
	font-size: 30px;
	cursor: pointer;
}


.diary-day-select i {
	cursor: pointer;
}

.diary-day-select i:hover {
	transform: scale(1.5);
}

</style>
