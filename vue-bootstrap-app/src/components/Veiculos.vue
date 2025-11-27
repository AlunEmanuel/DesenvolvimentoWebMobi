<template>
  <div>

    <vehicle-form
      v-if="view === 'form'"
      :initial-data="editItem"
      @saved="onSaved"
      @cancel="view = 'list'"
    />

   
    <vehicle-list
      v-if="view === 'list'"
      :veiculos="veiculos"
      @add="onAdd"
      @edit="onEdit"
      @refresh="fetchVeiculos"
    />
  </div>
</template>

<script>
import VehicleList from './VehicleList.vue'
import VehicleForm from './VehicleForm.vue'

export default {
  name: 'Veiculos',
  components: { VehicleList, VehicleForm },
  data() {
    return {
      view: 'list',   
      veiculos: [],
      editItem: null   
    };
  },
  methods: {
    onAdd() {
      this.editItem = null;
      this.view = 'form';
    },
    onEdit(item) {
      this.editItem = item;
      this.view = 'form';
    },
    onSaved(payload) {
      this.view = 'list';
    }
  }
};
</script>

<style scoped>
/* Adicione estilos locais se necessário */
</style>
