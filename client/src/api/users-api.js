import http from '@/http-client'

export default {
  fetch (id) {
    return http.get(`/api/users/${id}`).then(response => response.data)
  },
  create ({ username }) {
    return http.post('/api/users', { username }).then(response => response.data)
  },
}
