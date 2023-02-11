import api from './config.js'
import apiHelpers from './helpers.js'

export default {
  criarUsuario: (usuario) => {
    return api.post("/usuarios", usuario).then((response) => response.data)
  },

  listaFilmes: () => {
    return api.get("/api/letterboxd/filmes").then((response) => response.data)
  },

  adicionarFilme: (filme) => {
    return api.post("/api/letterboxd/adicionar", filme).then((response) => response.data)
  },

  pegarFilme: (filmeId) => {
     return api.get(`/api/letterboxd/filme/${filmeId}`).then((response) => response.data)
  },

  salvarFilmeEditado: (filme) => {
    return api.patch(`/api/letterboxd/editar/${filme.id}`, filme).then((response) => response.data)
  },

  excluirFilme: (filmeId) => {
    return api.delete(`/api/letterboxd/excluir/${filmeId}`).then((response) => response.data)
  },
}
