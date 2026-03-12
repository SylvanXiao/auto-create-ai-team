from pydantic import BaseModel
from typing import Optional, Literal

class CreateAITeamRequest(BaseModel):
    """创建AI团队的请求模型"""
    project_path: str
    project_type: Literal["generic", "custom"] = "generic"
    team_size: Literal["small", "medium", "large"] = "medium"
    models: Literal["free", "premium", "mixed"] = "mixed"

class CreateAITeamResponse(BaseModel):
    """创建AI团队的响应模型"""
    status: Literal["success", "error"]
    message: str
    team_path: Optional[str] = None
    team_info: Optional[dict] = None