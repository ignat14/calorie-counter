<template>
	<div>
		<div class="diary-day-select">
			<i class="fas fa-chevron-left" @click="go_left()"/>
			<VueCtkDateTimePicker v-model="current_date"
												:no-value-to-custom-elem="true"
												class="diary-day-picker"
												:only-date="true"
												format="YYYY-MM-DD"
												formatted="ll"
												@validate="changeDate"
												@is-hidden="changeDate"
			>
				<input class="diary-day-picker-title" v-model="formatted_date">
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
	computed: {
		formatted_date: function() {
			let today = new Date();
			const today_str = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
			const tomorrow_str = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+(today.getDate()+1);
			const yesterday_str = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+(today.getDate()-1);

			if (this.current_date == today_str) {
				return "Today";
			}
			else if (this.current_date == tomorrow_str) {
				return "Tomorrow";
			}
			else if (this.current_date == yesterday_str) {
				return "Yesterday";
			}
			
			let current_date = new Date(this.current_date).toDateString();
			let date_elems = current_date.split(" ").slice(1);
			let f_date = date_elems.join(' ');
			
			return f_date;
		}
	},
	methods: {
		changeDate: function() {
			this.$emit('input', this.current_date);
		},
		go_left: function() {
			let date = new Date(this.current_date);		
			let yesterday = date.getDate() - 1
			this.current_date = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+yesterday;
			this.$emit('input', this.current_date);
		},
		go_right: function() {
			let date = new Date(this.current_date);		
			let yesterday = date.getDate() + 1
			this.current_date = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+yesterday;
			this.$emit('input', this.current_date);
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
}

.diary-day-picker {
	display: flex;
	justify-content: center;
	width: 200px;
	margin: 0 20px;
}

.diary-day-picker-title {
	font-size: 1.6rem;
	width: 100%;
	background: none;
	border: none;
	text-align: center;
	cursor: pointer;
}

@media (max-width: 900px) {
	.diary-day-picker {
		width: 140px;
	}
}

.diary-day-select i {
	cursor: pointer;
}

.diary-day-select i:hover {
	transform: scale(1.5);
}

</style>
