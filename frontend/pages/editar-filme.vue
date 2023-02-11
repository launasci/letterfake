<template>
  <div>
    <forms-filmes
      :filme="filme"
      :titulo-card="tituloCard"
      :botao="botao"
      @salvarFilmeEditado="salvarFilmeEditado"
    />
  </div>
</template>

<script>
// import api from "@/api/apimock/apiMock.js";
import api from "@/api/api.js";
import formsFilmes from "@/components/forms-filmes.vue";

export default {
  components: {
    formsFilmes,
  },
  data: () => {
    return {
      categorias: [],
      filmes: [],
      tituloCard: "Edite um filme",        
      botao: "Editar",
       // objeto que envio para o forms-filme
      filme:{
        id: 0,
        status: "Pendente",
        categoria: "",
        titulo: "",
        descricao: "",
        imagem: "",
      }
    };
  },

  created() {
    this.listaFilmes();
    if (this.$route?.params?.id) {
      this.editarFilme(this.$route.params.id);
    }
  },

  methods: {
    listaFilmes() {
      api.listaFilmes().then(response => {
          this.filmes = response.filmes;
      });
    },

    setEditarFilme(recebido) {
      this.filme.id = recebido.id;
      this.filme.titulo = recebido.titulo;
      this.filme.categoria = recebido.categoria;
      this.filme.descricao = recebido.descricao;
      this.filme.status = recebido.status;
      this.filme.imagem = recebido.imagem  
    },
    
     async editarFilme(filmeId) {
      await api.pegarFilme(filmeId).then((response) =>{
          this.setEditarFilme(response.filme)
      })
    },
    salvarFilmeEditado(novoFilme) {
      api.salvarFilmeEditado(novoFilme).then(this.listaFilmes()),
      this.$router.push("/exibir-filmes");
    },
  },
};
</script>
