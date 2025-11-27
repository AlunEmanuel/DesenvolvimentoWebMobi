<template>
  <div class="vehicle-form">
    <h2>{{ isEditing ? 'Editar Veículo' : 'Cadastrar Veículo' }}</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="marca">Marca:</label>
        <input type="text" v-model="vehicle.marca" id="marca" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="modelo">Modelo:</label>
        <input type="text" v-model="vehicle.modelo" id="modelo" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="ano">Ano:</label>
        <input type="number" v-model="vehicle.ano" id="ano" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="cor">Cor:</label>
        <input type="text" v-model="vehicle.cor" id="cor" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="combustivel">Combustível:</label>
        <select v-model="vehicle.combustivel" id="combustivel" class="form-control" required>
          <option value="" disabled>Select</option>
          <option value="Gasolina">Gasolina</option>
          <option value="Álcool">Álcool</option>
          <option value="Diesel">Diesel</option>
          <option value="Elétrico">Elétrico</option>
        </select>
      </div>
      <div class="form-group">
        <label for="foto">Foto:</label>
        <input type="file" @change="onFileChange" id="foto" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">{{ isEditing ? 'Atualizar' : 'Cadastrar' }}</button>
    </form>
    <p>Modo: {{ action }} <span v-if="id">| ID: {{ id }}</span></p>
  </div>
</template>

<script>
export default {
  name: 'VehicleForm',
  props: {
    id: { type: [String, Number], default: null },
    action: { type: String, default: 'create' }
  }
};
</script>

<style scoped>
.vehicle-form {
  margin: 20px;
}
</style>