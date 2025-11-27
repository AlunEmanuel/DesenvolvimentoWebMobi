<template>
  <div id="app">
    <Navbar />
    <div class="container mt-4">
      <router-view />
      <VehicleList />
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import VehicleList from './components/VehicleList.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    VehicleList
  }
}
</script>

<style>
</style>
