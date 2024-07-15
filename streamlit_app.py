import streamlit as st
import akshare as ak

def get_futures_news(symbol, num_of_news):
    futures_news_shmet_df = ak.futures_news_shmet(symbol=symbol)
    futures_news_shmet_df = futures_news_shmet_df.sort_values(by="发布时间", ascending=False)
    selected_news_df = futures_news_shmet_df.head(num_of_news)
    formatted_news = selected_news_df.apply(lambda x: f"{x['发布时间']} - {x['内容']}", axis=1).tolist()
    return formatted_news

st.title('期货新闻查询')

symbol = st.selectbox('选择品种', ["全部", "要闻", "VIP", "财经", "铜", "铝", "铅", "锌", "镍", "锡", "贵金属", "小金属"])
num_of_news = st.number_input('输入查看的最新新闻条数', min_value=1, step=1)

if st.button('查询'):
    news_list = get_futures_news(symbol, num_of_news)
    for news in news_list:
        st.write(news)
