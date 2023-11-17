const axios = require('axios')

module.exports = async (req, res) => {
    const user_message = req.body.message

    try {
        const response = await axios.post("https://openkey.cloud/v1/chat/completions",
            {
                "model": "gpt-4-0613",
                "messages": [{"role": "user", "content": user_message}]
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer sk-91OdInYu1FVFaOjIlZhp0gI1i7jkpaduiEvsKAtqOsQLctlB'  
                }
            }
        )
        return res.status(200).json(response.data.choices[0].message.content)
    } catch (error) {
        console.error(error)
        return res.status(500).json({ error: 'Error in getting response from GPT-4' })
    }
}
