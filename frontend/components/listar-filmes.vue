<template>
  <v-container class="d-flex flex-row mt-5 full">
    <div class="d-flex flex-column width pesquisar">
      <v-col
        cols="11"
        offset="1"
      >
        <v-text-field
          v-model="pesquisa"
          color="deep-orange darken-1"
          :loading="loading"
          placeholder="Encontre um filme ou serie"
        /><porcentagem-categorias :porcentagem="porcentagem" />

        <v-btn
          class="mt-4 mr-4"
          dark
          small
          width="783"
          height="40"
          color="deep-orange darken-1"
          @click="adicionarNovoFilme"
        >
          adicionar
        </v-btn>
        <v-img
          class="ml-16 mt-16"
          height="700"
          width="700"
        />
      </v-col>
    </div>

    <div class="d-flex flex-column width mt-13">
      <v-col
        cols="12"
        offset="1"
      >
        <v-row class="linha">
          <v-card
            v-for="filme, index in filmesFiltrados"
            :key="filme.id"
            width="350"
            max-height="900"
            class="mx-2 my-2"
          >
            <v-card-title>
              {{ filme.titulo }}
              <v-spacer />
              <v-chip
                label
                class="yellow darken-2 black--text"
              >
                {{ String(filme.status) }}
              </v-chip>
              <v-img
                height="450"
                class="my-2"
                :src="filme.imagem"
              />
            </v-card-title>
            <v-expand-transition>
              <div v-show="listCardShow.includes(index)">
                <v-divider />
                <v-card-text class="font-weight-medium text-md-body-1 text-justify">
                  {{ filme.descricao }}
                </v-card-text>
              </div>
            </v-expand-transition>
            <div class="d-flex tags">
              <v-chip
                label
                class="yellow darken-2  black--text"
              >
                {{ String(filme.categoria) }}
              </v-chip>
              <v-btn
                dark
                small
                width="80"
                height="32"
                color="black"
                @click="selecionarFilmeEdicao(filme.id)"
              >
                editar
              </v-btn>
              <v-btn
                dark
                width="80"
                small
                height="32"
                color="black"
                @click="excluirFilme(filme.id)"
              >
                excluir
              </v-btn>
              <v-card-actions>
                <v-btn
                  icon
                  @click="toggleItem(index, listCardShow)"
                >
                  <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                </v-btn>
              </v-card-actions>
            </div>
          </v-card>
        </v-row>
      </v-col>
    </div>
  </v-container>
</template>

<script>
import porcentagemCategorias from "@/components/porcentagem-categorias.vue";
export default {
  components: {
    porcentagemCategorias,
  },
  props: ['filmes'],
  data: () => {
    return {
      pesquisa: "",
      show: false,
      listCardShow: [], 
      loading: false
    };
  },

  computed: {
    filmesFiltrados() {
      return this.filmes.filter((e) => {
        return e.titulo.toLowerCase().includes(this.pesquisa.toLowerCase());
      });
    },
    porcentagem() {
      const porcentagem = {
        Terror: 0,
        Drama: 0,
        Comedia: 0,
        Ação: 0,
        Outros: 0
      }
      for (let filme of this.filmes) {
        porcentagem[filme.categoria] += (1  / this.filmes.length) * 100
      }
      return porcentagem
    }
  },
  methods: {
    selecionarFilmeEdicao(filmeId) {
      this.$emit("selecionarFilmeEdicao", filmeId);
    },

    excluirFilme(filmeId) {
      this.$emit("excluirFilme", filmeId);
    },

    adicionarNovoFilme(novoFilme) {
      this.$emit("adicionarNovoFilme", novoFilme);
      // :src="require('../static/img-home.png')"
    },
    toggleItem(item, _array){
        if(_array.includes(item)){
          const i = _array.indexOf(item)
          _array.splice(i, 1)
        }
        else{
         _array.push(item)
        }
    }
  },
};
</script>

<style scoped>
.full {
  width: 100vw;
}
.width {
  width: 50vw;
}
.tags{
  justify-content: space-evenly !important;
  margin-bottom: 20px;
}
.v-card__actions {
    padding: 0 !important;
}
</style>
