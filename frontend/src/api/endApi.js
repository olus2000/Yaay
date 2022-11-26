import axios from "axios";

export const handleEndGet = async (getter, id) => {
  await axios.get(`http://localhost:5000/api/end/${id}`).then(e => getter(e.data));
}