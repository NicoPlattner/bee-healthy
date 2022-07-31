<template>
	<MainScreen v-if="this.menuOption === 0"></MainScreen>
	<ChatScreen v-if="this.menuOption === 1"></ChatScreen>
</template>

<script>
import MainScreen from "@/pages/DataScreen";
import ChatScreen from "@/pages/ChatScreen";

export default {
	name: "BodyComponent",
	components: {
		ChatScreen,
		MainScreen
	},
	data() {
		return {
			menuOption: 0,
		}
	},
	mounted() {
		this.emitter.on('select', option => {

			this.menuOption = option;
			console.log(this.menuOption)

		})
	}
}
</script>

<style scoped>

</style>
