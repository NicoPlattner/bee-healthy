<template>
	<div style="margin: 4em 2em">
		<div v-for="message in messages" v-bind:key="message" style="width: 70%; margin-bottom: .5em; background-color: #FFCD32; padding: .5em 1em; border-radius: 1em; float: right">
			{{ message }}
		</div>
	</div>


	<div style="position:absolute; top: calc(100% - 8em); border-top: 1px solid black; width: 100vw">
		<form @submit.prevent="this.send($event); ">
			<div class="form-group" style="margin: 0.7em 0.6em; width: 80%; float: left">
				<input type="text" class="form-control">
			</div>
			<div style="width: 10%; float: left; font-size: 2em; text-align: center; margin-top: 0.25em">
				<i class="bi bi-paperclip"></i>
			</div>
		</form>
	</div>
</template>

<script>
export default {
	name: "ChatScreen",
	data() {
		return {
			messages: []
		}
	},
	methods: {
		send(message) {
			this.messages.push(message.target[0].value)
			message.target[0].value = '';
		}
	}
}
</script>

<style scoped>

</style>
