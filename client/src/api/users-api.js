import http from '@/http-client'

export default {
  fetch (id) {
    return http.get(`/api/users/${id}`).then(response => response.data)
  },
}
