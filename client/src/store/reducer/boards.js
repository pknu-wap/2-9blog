import produce from 'immer';
import { createAction, createReducer } from '@reduxjs/toolkit';
import { v4 as uuid } from 'uuid';

export const CREATE_BOARD = "todo/CREATE_BOARD";
export const DELETE_BOARD = "todo/DELETE_BOARD";

//define createBoard action 
export const createBoard = createAction(CREATE_BOARD, function prepare(title) {
    return {
        payload: {
            id: uuid(),
            title : title,
            createdAt: new Date().toISOString(),
        }
    }
});

export const deleteBoard = createAction(DELETE_BOARD, function prepare(boardId){
    return {
        payload:{
            boardId : boardId 
        }
    }
})

const actions = {
    createBoard
};

export { actions };

const initialState = {
    boards: [{
        id: "",
        title: ""
    }]
};

export default createReducer(initialState, {
    [CREATE_BOARD]: (state, action) => {
        return produce(state, draft => {
            draft.boards = [...state.boards, { id: action.payload.id, title: action.payload.title }];
        })
    },
    [DELETE_BOARD]: (state, action) => {
        return produce(state, draft => {
            draft.boards = state.boards.filter((board)=> board.id !== action.payload.boardId);
        })
    }
});
/*produce는 불변성을 관리할 수 있는 immer를 불러온 것으로
  (수정하고 싶은 상태, 업데이트 정의 함수)로 넣어준다.*/
  