async function analyze(text) {
    const language = require('@google-cloud/language');

    const client = new language.LanguageServiceClient();
    const document = {
        content: text,
        type: 'PLAIN_TEXT'
    };

    const [result] = await client.analyzeSentiment({
        document
    });
    const sentiment = result.documentSentiment;

    return {
        score: sentiment.score,
        magnitude: sentiment.magnitude
    }
}

module.exports = {
    analyze
}