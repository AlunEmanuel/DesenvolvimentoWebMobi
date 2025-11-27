<template>
  <div class="vehicle-list">
    <p>Lista de Veículos</p>
    <table v-if="vehicles && vehicles.length" class="table table-bordered table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Marca</th>
          <th>Modelo</th>
          <th>Ano</th>
          <th>Cor</th>
          <th>Combustível</th>
          <th>Foto</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="v in vehicles" :key="v.id">
          <td>{{ v.id }}</td>
          <td>{{ v.get_marca_display || v.marca }}</td>
          <td>{{ v.modelo }}</td>
          <td>{{ v.ano }}</td>
          <td>{{ v.get_cor_display || v.cor }}</td>
          <td>{{ v.get_combustivel_display || v.combustivel }}</td>
          <td>
            <img v-if="v.foto && v.foto.url" :src="v.foto.url" alt="Foto" width="100" />
            <span v-else>Sem foto</span>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>Nenhum veículo cadastrado.</p>
  </div>
</template>

<script>
export default {
  name: 'VehicleList',
  props: {
    vehicles: {
      type: Array,
      default: () => []
    }
  }
};
</script>

<style scoped>
/* Estilos específicos para o componente VehicleList */
.table {
  width: 100%;
  margin-top: 10px;
}
</style>
