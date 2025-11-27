<template>
	<div class="home-view">
		<h1>Veículos</h1>
		<VehicleList />
	</div>
</template>

<script>
import VehicleList from '../components/VehicleList.vue';
export default {
	name: 'Home',
	components: { VehicleList }
};
</script>

<style scoped>
.home-view {
  padding: 20px;
}
</style>
