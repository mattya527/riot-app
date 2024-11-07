import React, { Fragment, useState, } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, TextField, Button, Typography, Box, Stack } from '@mui/material';

const UserNameForm = () => {
    const [user_name, setUserName] = useState('')
    const [tag_line, setTagLine] = useState('')
    const navigate = useNavigate()
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log('Submited username : ',user_name)
      console.log('Submited tagline : ', tag_line)
      try{
        if(user_name === '' || tag_line === ''){
          alert('Please fill the username and tagline')
          return
        }
        navigate('/match-history-list', { state : { user_name, tag_line }})
      }catch(error){
        console.log('Error submitting :',error)
        alert('Failed to submit username. Please try again.')
      }
    }
  
    return (
        <Fragment>
            <Container maxWidth="sm" sx={{ mt : 5 }}>
                <Box
                component="form"
                onSubmit={handleSubmit}
                sx={{
                    display : 'flex',
                    flexDirection : 'column',
                    alignItems : 'center',
                    p : 4,
                    borderRadius : 2,
                    boxShadow : 3,
                    backgroundColor : '#f5f5f5',
                }}
                >
                <Typography variant='h5' sx={{ mb : 2}}>
                    IDを入力
                </Typography>
                <Stack direction='row' spacing={2} sx={{ mb : 3, width : '100%' }}>
                    <TextField
                        label='Username'
                        variant='outlined'
                        fullWidth
                        sx={{ mb : 3}}
                        value={user_name}
                        onChange={(e) => setUserName(e.target.value)}
                    />
                    <TextField
                        label='tagline'
                        variant='outlined'
                        fullWidth
                        sx={{ mb : 3}}
                        value={tag_line}
                        onChange={(e) => setTagLine(e.target.value)}
                    />
                    </Stack>
                    <Button
                        type='submit'
                        variant='contained'
                        color='primary'
                        fullWidth
                        sx={{ p : 1.5}}
                    >
                        Submit
                    </Button>
                </Box>
            </Container>
        </Fragment>
    )
  }

  export default UserNameForm