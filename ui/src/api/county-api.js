import http from '@/lib/http-client'

export default {
  fetch (id) {
    return http.get(`/api/county/${id}`).then(response => {
      return response.data
    })
  },
}
