import React from "react";
import { useHistory, useParams, Link } from "react-router-dom";
import { Card, Button, Container, Row } from "react-bootstrap";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import Posts from "./Posts";
import { useSelector } from "react-redux";
import Threads from "./Threads";
const Board = (props) => {
  const params = useParams();

  const history = useHistory();
  const board = useSelector((state) => {
    return state.appstate.boardData.find((e) => e.id === params.boardid);
  });
  const favoritePosts = useSelector((state) => {
    return state.appstate.favoritePosts;
  });
  const addToFavorite = () => {
    favoritePosts.push(boards.id);
    console.log(favoritePosts);
  };
  const boards = props.boards || board;

  // const boards = props.boards || history.location.state.boards;
  const postsData = useSelector((state) => {
    return state.appstate.postArr;
  });

  const isLoading = useSelector((state) => {
    return state.appstate.isLoading;
  });

  const postSearch = useSelector((state) => {
    return state.appstate.postSearch;
  });

  if (isLoading) return <div>Loading...</div>;
  return (
    <div>
      <Container>
        <Row>
          <Card
            style={{ width: "100%", height: "200px" }}
            className="bg-dark text-white"
          >
            <Card.Img
              style={
                {
                  // width: "200px",
                  // height: "200px",
                  // display: "block",
                  // marginLeft: "auto",
                  // marginRight: "auto",
                  // width: "50%",
                }
              }
              src=""
              alt="Card image"
            />
            <Card.ImgOverlay style={{}}>
              <Card.Title style={{}}>{boards.title}</Card.Title>
              <Card.Text>{boards.description}</Card.Text>

              <Button
                className="commentBu"
                onClick={() => history.push(`/threadpost/${boards.id}`)}
              >
                add thread
              </Button>
              <Button
                style={{ marginLeft: "3px" }}
                className="commentBu"
                onClick={() => addToFavorite()}
              >
                add to fivorits
              </Button>
            </Card.ImgOverlay>
          </Card>
          <Threads boardid={boards.id} />
        </Row>
      </Container>
      <br />
    </div>
  );
};
const redux = (dispatch) => bindActionCreators({}, dispatch);
export default connect(null, redux)(Board);
