<template>
	<div style="top: calc(100% - 4em); position: fixed">
		<div style="border-top: 1px solid black;">
			<div @click="this.selectMenuOption(0)" onclick="" style="font-size: 2.5em; margin-top: .1em; height: 4em; width: 50vw; text-align: center; float: left; border-right: 1px solid black">
				<i class="bi bi-bar-chart-fill"></i>
			</div>
			<div @click="this.selectMenuOption(1)" style="font-size: 2.5em; margin-top: .1em; height: 4em; width: 50vw; text-align: center; float: left; border-right: 1px solid black">
				<i class="bi bi-chat-dots"></i>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "NavBar",
	methods: {
		selectMenuOption(optionId) {
			this.emitter.emit('select', optionId);
		}
	}
}
</script>

<style scoped>

</style>
