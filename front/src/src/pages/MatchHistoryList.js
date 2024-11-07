import React,{ useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Container, Typography, Box, List, ListItem, ListItemText } from '@mui/material';

const MatchHistoryList = () => {
    const location = useLocation()
    const { user_name, tag_line } = location.state
    const [data, setData] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            try{
                const params = {
                    user_name : user_name,
                    tag_line : tag_line,
                    region : 'Asia'
                }
                const query = new URLSearchParams(params)
                const response = await fetch(`http://localhost:8005/getMatchHistoryList?${query}`,{
                    method : 'GET',
                    headers : {
                        'Content-Type' : 'application/json',
                    }
                })
                if(!response.ok){
                    throw new Error('API request failed')
                }
                const result = await response.json()
                console.log('API Response :', result)
                setData(result);
            }catch(error){
                console.log('Error fetching data :',error)
            }
        }
        if (user_name && tag_line){
            fetchData()
        }
        },[user_name, tag_line])

    return (
        <Container>
            <Box mt={3}>
                <Typography variant="h6">{user_name}#{tag_line}のマッチ履歴</Typography>
                
                {data ? (
                    <List>
                        {data.match_list.map((match, index) => (
                            <ListItem key={index}>
                                <ListItemText
                                    primary={`Match ${index + 1}`}
                                    secondary={JSON.stringify(match, null, 2)}
                                />
                            </ListItem>
                        ))}
                    </List> 
                ) : (
                    <Typography>データを取得中...</Typography>
                )}
            </Box>
        </Container>
    );
}

export default MatchHistoryList;