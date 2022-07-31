<template>
	<div>
		<b-row style="height: 3em" v-if="problemHives.length === 0 && downHives.length === 0">
			<b-col cols="12">
				<div class='square-box'>
					<div style="background-color: green" class='square-content'>
						<div class="app-content">
							No problems
						</div>
					</div>
				</div>
			</b-col>
		</b-row>

		<div v-if="problemHives.length !== 0">
			<b-row style="height: 3em; margin-bottom: 5em" v-for="hive in problemHives" v-bind:key="hive.id">
				<b-col cols="12">
					<div class='square-box'>
						<div style="background-color: orangered" class='square-content'>
							<div class="app-content">
								Health of {{ hive.name }} critical!
							</div>
						</div>
					</div>
				</b-col>
			</b-row>
		</div>

		<div v-if="downHives.length !== 0">
			<b-row style="height: 3em; margin-bottom: 5em" v-for="hive in downHives" v-bind:key="hive.id">
				<b-col cols="12">
					<div class='square-box'>
						<div style="background-color: darkgray" class='square-content'>
							<div class="app-content">
								{{ hive.name }} is down
							</div>
						</div>
					</div>
				</b-col>
			</b-row>
		</div>
	</div>
</template>

<script>
export default {
	name: "OverviewPage",
	data() {
		return {
			hives: [],
			problemHives: [],
			downHives: []
		}
	},
	mounted() {
		fetch('http://localhost:5000/getAllHives/0')
		.then((response) => response.json())
		.then((data) => {
			this.hives = data;

			this.hives.forEach(hive => {
				if(hive.sensorData.predictedHealthStatus[hive.sensorData.predictedHealthStatus.length - 1] < 50) {
					this.problemHives.push(hive);
				}
			})

			this.hives.forEach(hive => {
				const sensorTime = hive.sensorData.epochTime[hive.sensorData.epochTime.length - 1];
				if(sensorTime > Math.floor(new Date().getTime() / 1000) + 7200000) { //2 hours difference
					this.downHives.push(hive);
				}
			})
		});
	}
}
</script>

<style scoped>
.app-content {
	margin-top: .5em;
	font-size: .6em;
	text-align: center;
}

.square-box {
	position: relative;
	overflow: hidden;
	width: 100%;
	margin-right: 10%;
	background: #FFCD32;
	border-radius: .7em;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-box:before {
	content: "";
	display: block;
	padding-top: 30%;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-content {
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	color: black;
	font-size: 2.5em;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}
</style>
