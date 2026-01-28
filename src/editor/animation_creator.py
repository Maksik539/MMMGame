"""
Animation creator utility for generating animation JSON files
"""
import json
import os


class AnimationCreator:
    """Utility for creating animation definition files"""
    
    @staticmethod
    def create_animation_file(name, frames, frame_duration=5, output_dir="assets/animations"):
        """Create an animation JSON file"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        data = {
            "name": name,
            "frame_duration": frame_duration,
            "frames": frames,
            "looping": True
        }
        
        filepath = os.path.join(output_dir, f"{name}.json")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
        return filepath
        
    @staticmethod
    def create_basic_animations():
        """Create some basic animation templates"""
        animations = [
            {
                "name": "idle",
                "frames": [{"sprite": "player_idle_0"}, {"sprite": "player_idle_1"}],
                "frame_duration": 10
            },
            {
                "name": "walk",
                "frames": [
                    {"sprite": "player_walk_0"},
                    {"sprite": "player_walk_1"},
                    {"sprite": "player_walk_2"},
                    {"sprite": "player_walk_3"}
                ],
                "frame_duration": 5
            }
        ]
        
        for anim_data in animations:
            AnimationCreator.create_animation_file(
                anim_data["name"],
                anim_data["frames"],
                anim_data["frame_duration"]
            )
