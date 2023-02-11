<template>
  <div>
    <v-col
      cols="4"
      offset="4"
      class="form d-flex"
    >
      <v-card>
        <v-card-title>
          <span class="text-h6">{{ tituloCard }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  v-model="novoFilme.titulo"
                  class="text-h7"
                  type="text"
                  placeholder="Titulo"
                />
              </v-col>
              <v-col cols="6">
                <v-autocomplete
                  v-model="novoFilme.status"
                  :items="['Visto', 'Quero ver', 'Sem interesse']"
                  label="Status"
                />
              </v-col>
              <v-col cols="6 mt-8">
                <v-autocomplete
                  v-model="novoFilme.categoria"
                  :items="['Terror', 'Comedia', 'Ação', 'Drama', 'Outros']"
                  label="Categorias"
                />
              </v-col>
              <v-col cols="6 mt-8">
                <v-text-field
                  v-model="novoFilme.imagem"
                  prepend-icon="mdi-camera"
                  label="Adicione uma foto"
                />
              </v-col>
              <v-textarea
                v-model="novoFilme.descricao"
                auto-grow
                :rules="rules"
                class="text-h9"
                placeholder="Adicione uma descrição"
              />
            </v-row>
            <v-btn
              color="deep-orange darken-1"
              dark
              bottom
              class="mt-10"
              @click="salvarFilme"
            >
              {{ botao }}
            </v-btn>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-col>
  </div>
</template>

<script>
export default {
  props: ['filme', 'tituloCard', 'botao'],

  data: () => {
    return {
      rules: [v => v.length <= 140 || 'Sem textão'],
      novoFilme: {
        titulo: '',
        descricao: '',
        status: '',
        categoria: '',
        id: 0,
        imagem: '',
      }
    };
  },

  mounted(){
    this.novoFilme = this.filme
  },

  methods: {
    salvarFilme() {
      if (this.botao == "Adicionar") {
        this.$emit("salvarFilme", this.novoFilme);
      } else {
        this.novoFilme = this.novoFilme
        this.$emit("salvarFilmeEditado", this.novoFilme);
      }
    },
  },
};
</script>

<style scoped>
.form {
  margin-top: 8% !important;
}
</style>
