import axios from "axios";


export const handleStartGet = async (getter, eventId) => {
  console.log(eventId);
  await axios.get(`http://localhost:5000/api/start/${eventId}`).then(e => getter(e.data));
}